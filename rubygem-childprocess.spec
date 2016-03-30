#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : rubygem-childprocess
Version  : 0.5.9
Release  : 6
URL      : https://rubygems.org/downloads/childprocess-0.5.9.gem
Source0  : https://rubygems.org/downloads/childprocess-0.5.9.gem
Summary  : No detailed summary available
Group    : Development/Tools
License  : MIT
BuildRequires : ruby
BuildRequires : rubygem-bundler
BuildRequires : rubygem-coveralls
BuildRequires : rubygem-rdoc
BuildRequires : rubygem-rspec
BuildRequires : rubygem-rspec-core
BuildRequires : rubygem-yard

%description
# childprocess
This gem aims at being a simple and reliable solution for controlling
external programs running in the background on any Ruby / OS combination.

%prep
gem unpack %{SOURCE0}
%setup -q -D -T -n childprocess-0.5.9
gem spec %{SOURCE0} -l --ruby > rubygem-childprocess.gemspec

%build
gem build rubygem-childprocess.gemspec

%install
%global gem_dir $(ruby -e'puts Gem.default_dir')
gem install -V \
--local \
--force \
--install-dir .%{gem_dir} \
--bindir .%{_bindir} \
childprocess-0.5.9.gem

mkdir -p %{buildroot}%{gem_dir}
cp -pa .%{gem_dir}/* \
%{buildroot}%{gem_dir}

if [ -d .%{_bindir} ]; then
mkdir -p %{buildroot}%{_bindir}
cp -pa .%{_bindir}/* \
%{buildroot}%{_bindir}/
fi


%files
%defattr(-,root,root,-)
/usr/lib64/ruby/gems/2.3.0/cache/childprocess-0.5.9.gem
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/.document
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/.gitignore
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/.rspec
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/.travis.yml
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/Gemfile
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/LICENSE
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/README.md
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/Rakefile
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/childprocess.gemspec
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/abstract_io.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/abstract_process.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/errors.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/jruby.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/jruby/io.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/jruby/process.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/jruby/pump.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/tools/generator.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/unix.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/unix/fork_exec_process.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/unix/io.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/unix/lib.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/unix/platform/i386-linux.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/unix/platform/i386-solaris.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/unix/platform/x86_64-linux.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/unix/platform/x86_64-macosx.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/unix/posix_spawn_process.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/unix/process.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/version.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/windows.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/windows/handle.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/windows/io.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/windows/lib.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/windows/process.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/windows/process_builder.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/lib/childprocess/windows/structs.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/spec/abstract_io_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/spec/childprocess_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/spec/io_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/spec/jruby_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/spec/pid_behavior.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/spec/spec_helper.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/spec/unix_spec.rb
/usr/lib64/ruby/gems/2.3.0/gems/childprocess-0.5.9/spec/windows_spec.rb
/usr/lib64/ruby/gems/2.3.0/specifications/childprocess-0.5.9.gemspec
